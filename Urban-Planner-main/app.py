import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pydeck as pdk
import requests
import json
import io
import base64
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import geopandas as gpd
from shapely.geometry import Point
import folium
from streamlit_folium import folium_static
import networkx as nx

import streamlit as st

# Gemini API configuration
API_KEY = "AIzaSyC5JOsQ53AcrgqL5_3fsxdX4mLOxTr_JA4"
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

import pandas as pd
import streamlit as st

@st.cache
def load_data(file):
    try:
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.name.endswith('.xlsx'):
            df = pd.read_excel(file)
        else:
            st.error("Unsupported file format. Please upload a CSV or Excel file.")
            return None
        
        required_columns = ['lat', 'lon', 'population', 'traffic', 'green_space']
        if not all(col in df.columns for col in required_columns):
            st.error(f"File must contain the following columns: {', '.join(required_columns)}")
            return None
        
        return df
    except Exception as e:
        st.error(f"Error loading file: {str(e)}")
        return None


def generate_synthetic_data(num_areas=100, time_periods=5):
    np.random.seed(42)
    data = []
    for period in range(time_periods):
        for area in range(1, num_areas + 1):
            data.append({
                'time_period': period,
                'area_id': area,
                'lat': np.random.uniform(40.0, 42.0),
                'lon': np.random.uniform(-74.0, -73.0),
                'population': np.random.randint(1000, 100000),
                'traffic': np.random.randint(100, 10000),
                'green_space': np.random.uniform(1, 30),
                'crime_rate': np.random.uniform(0, 10),
                'avg_income': np.random.randint(30000, 150000),
                'public_transport_access': np.random.uniform(0, 100),
                'air_quality_index': np.random.uniform(0, 200),
                'housing_density': np.random.uniform(10, 1000),
                'commercial_area_percentage': np.random.uniform(5, 50),
                'healthcare_facilities': np.random.randint(1, 20),
                'education_facilities': np.random.randint(1, 30),
                'energy_consumption': np.random.uniform(100, 1000),
                'water_usage': np.random.uniform(50, 500),
                'waste_generation': np.random.uniform(10, 100),
                'internet_connectivity': np.random.uniform(60, 100),
                'elderly_population_percentage': np.random.uniform(5, 30)
            })
    df = pd.DataFrame(data)
    return df

def download_csv(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="urban_planning_data.csv">Download Data (CSV)</a>'
    return href

def call_gemini_api(prompt):
    try:
        headers = {"Content-Type": "application/json"}
        data = {"contents": [{"parts": [{"text": prompt}]}]}
        response = requests.post(f"{API_URL}?key={API_KEY}", headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"API call failed: {str(e)}")
        return None

def visualize_data(df, color_factor):
    st.subheader("Advanced City Data Visualization")
    
    # Create a GeoDataFrame
    gdf = gpd.GeoDataFrame(
        df, geometry=gpd.points_from_xy(df.lon, df.lat), crs="EPSG:4326"
    )
    
    # Folium map
    m = folium.Map(location=[df.lat.mean(), df.lon.mean()], zoom_start=10)
    
    # Add choropleth layer
    folium.Choropleth(
        geo_data=gdf.geometry.__geo_interface__,
        name="choropleth",
        data=df,
        columns=["area_id", color_factor],
        key_on="feature.id",
        fill_color="YlOrRd",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=color_factor
    ).add_to(m)
    
    # Add circle markers
    for idx, row in df.iterrows():
        folium.CircleMarker(
            location=[row.lat, row.lon],
            radius=5,
            popup=f"Area {row.area_id}<br>{color_factor}: {row[color_factor]}",
            color="blue",
            fill=True,
            fillColor="blue"
        ).add_to(m)
    
    folium_static(m)
    
    # 3D visualization with Pydeck
    layer = pdk.Layer(
        "HexagonLayer",
        data=df,
        get_position=["lon", "lat"],
        elevation_scale=50,
        elevation_range=[0, 1000],
        pickable=True,
        extruded=True,
        coverage=1,
    )
    view_state = pdk.ViewState(latitude=df["lat"].mean(), longitude=df["lon"].mean(), zoom=9, pitch=50)
    r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "\n".join(f"{col}: {{{{ {col} }}}}" for col in df.columns)})
    st.pydeck_chart(r)

    # Correlation Network Graph
    st.subheader("Correlation Network Graph")
    corr = df.corr()
    G = nx.Graph()
    for i in range(len(corr.columns)):
        for j in range(i+1, len(corr.columns)):
            if abs(corr.iloc[i, j]) > 0.5:  # Only show strong correlations
                G.add_edge(corr.columns[i], corr.columns[j], weight=abs(corr.iloc[i, j]))

    fig, ax = plt.subplots(figsize=(12, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, ax=ax, with_labels=True, node_color='lightblue', 
            node_size=3000, font_size=8, font_weight='bold')
    
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
    
    plt.title("Urban Factors Correlation Network")
    st.pyplot(fig)

def analyze_data(df):
    st.subheader("Advanced Data Analysis")

    # Correlation analysis
    corr = df.corr()
    fig_corr = px.imshow(corr, text_auto=True, aspect="auto")
    st.plotly_chart(fig_corr)

    # Advanced clustering analysis
    features = ['population', 'traffic', 'green_space', 'crime_rate', 'avg_income', 'public_transport_access', 
                'air_quality_index', 'housing_density', 'commercial_area_percentage', 'energy_consumption', 
                'water_usage', 'waste_generation', 'internet_connectivity', 'elderly_population_percentage']
    X = df[features]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # K-means clustering
    kmeans = KMeans(n_clusters=5, random_state=42)
    df['kmeans_cluster'] = kmeans.fit_predict(X_scaled)
    
    # DBSCAN clustering
    dbscan = DBSCAN(eps=0.5, min_samples=5)
    df['dbscan_cluster'] = dbscan.fit_predict(X_scaled)
    
    # PCA for visualization
    pca = PCA(n_components=3)
    X_pca = pca.fit_transform(X_scaled)
    
    fig_cluster = px.scatter_3d(x=X_pca[:, 0], y=X_pca[:, 1], z=X_pca[:, 2], 
                                color=df['kmeans_cluster'],
                                symbol=df['dbscan_cluster'],
                                labels={'x': 'PC1', 'y': 'PC2', 'z': 'PC3'},
                                title='Cluster Analysis (PCA)')
    st.plotly_chart(fig_cluster)

    # Feature importance analysis
    st.subheader("Feature Importance Analysis")
    target = st.selectbox("Select target variable for importance analysis", features)
    X = df[features]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    
    importance = pd.DataFrame({'feature': features, 'importance': rf.feature_importances_})
    importance = importance.sort_values('importance', ascending=False)
    
    fig_importance = px.bar(importance, x='feature', y='importance', title=f'Feature Importance for {target}')
    st.plotly_chart(fig_importance)
    
    # Model performance
    y_pred = rf.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    st.write(f"Mean Squared Error: {mse:.2f}")
    st.write(f"R-squared Score: {r2:.2f}")

def generate_urban_proposal(df, focus_area):
    city_data = df.to_dict(orient="records")
    prompt = f"""Analyze this urban data and suggest detailed development proposals focusing on {focus_area}. 
    Include specific recommendations for infrastructure changes, policy adjustments, and potential impact on quality of life. 
    Consider the following aspects in your analysis:
    1. Population density and distribution
    2. Traffic patterns and public transportation access
    3. Green space availability
    4. Crime rates and safety measures
    5. Economic factors (average income)
    6. Sustainability and environmental impact (air quality, energy consumption, water usage, waste generation)
    7. Housing density and commercial area distribution
    8. Healthcare and education facilities
    9. Internet connectivity and smart city initiatives
    10. Elderly population needs

    Data summary: {json.dumps(city_data[:10])}  # Sending only first 10 records to avoid token limit
    
    Provide a comprehensive plan with short-term and long-term goals, potential challenges, and expected outcomes. 
    Include innovative solutions, consider the interplay between different urban factors, and suggest data-driven policy recommendations."""
    
    response = call_gemini_api(prompt)
    
    if response and "candidates" in response:
        proposals = response["candidates"][0]["content"]["parts"][0]["text"]
        st.subheader("Urban Development Proposals")
        st.write(proposals)
        return proposals
    else:
        st.error("Failed to generate proposals. Please try again.")
        return None

def create_pdf_report(df, proposals):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Title
    elements.append(Paragraph("Advanced AI-Driven Urban Planning Report", styles['Title']))
    elements.append(Spacer(1, 12))

    # Data Summary
    elements.append(Paragraph("City Data Summary", styles['Heading2']))
    data_summary = df.describe().reset_index().values.tolist()
    data_summary.insert(0, ['Statistic'] + list(df.describe().columns))
    t = Table(data_summary)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(t)
    elements.append(Spacer(1, 12))

    # Data Visualizations
    elements.append(Paragraph("Data Visualizations", styles['Heading2']))
    
    # Correlation heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.savefig('correlation_heatmap.png')
    elements.append(Paragraph("Correlation Heatmap", styles['Heading3']))
    elements.append(Spacer(1, 12))
    elements.append(Image('correlation_heatmap.png', width=400, height=300))
    elements.append(Spacer(1, 12))

    # Urban Development Proposals
    elements.append(Paragraph("Urban Development Proposals", styles['Heading2']))
    elements.append(Paragraph(proposals, styles['BodyText']))

    doc.build(elements)
    buffer.seek(0)
    return buffer

def export_report(df, proposals):
    pdf_buffer = create_pdf_report(df, proposals)
    b64 = base64.b64encode(pdf_buffer.getvalue()).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="advanced_urban_planning_report.pdf">Download Detailed PDF Report</a>'
    st.markdown(href, unsafe_allow_html=True)

def calculate_sustainability_score(df):
    green_space_score = df['green_space'].mean() / 30 * 2
    air_quality_score = (200 - df['air_quality_index'].mean()) / 200 * 2
    public_transport_score = df['public_transport_access'].mean() / 100 * 2
    energy_efficiency_score = (1000 - df['energy_consumption'].mean()) / 1000 * 2
    water_management_score = (500 - df['water_usage'].mean()) / 500 * 2
    
    total_score = green_space_score + air_quality_score + public_transport_score + energy_efficiency_score + water_management_score
    return total_score

def predict_future_trends(df):
    features = ['population', 'traffic', 'green_space', 'air_quality_index', 'public_transport_access']
    predictions = {}
    
    for feature in features:
        # Prepare data
        data = df.groupby('time_period')[feature].mean().reset_index()
        
        # Train a Gradient Boosting model
        X = data['time_period'].values.reshape(-1, 1)
        y = data[feature].values
        model = GradientBoostingRegressor(n_estimators=100, random_state=42)
        model.fit(X, y)
        
        # Predict next 5 time periods
        future_periods = np.array(range(data['time_period'].max() + 1, data['time_period'].max() + 6)).reshape(-1, 1)
        future_predictions = model.predict(future_periods)
        
        # Calculate trend
        current_value = data[feature].iloc[-1]
        future_value = future_predictions[-1]
        trend = "Increasing" if future_value > current_value else "Decreasing"
        
        predictions[feature] = {
            "current_value": current_value,
            "predicted_values": future_predictions.tolist(),
            "trend": trend
        }
    
    return predictions

def recommend_smart_city_tech(df):
    recommendations = []
    if df['traffic'].mean() > 5000:
        recommendations.append("Implement smart traffic management systems")
    if df['air_quality_index'].mean() > 100:
        recommendations.append("Deploy IoT-based air quality monitoring network")
    if df['public_transport_access'].mean() < 50:
        recommendations.append("Introduce smart public transport tracking and scheduling")
    if df['energy_consumption'].mean() > 500:
        recommendations.append("Implement smart grid technologies for better energy management")
    if df['water_usage'].mean() > 250:
        recommendations.append("Deploy smart water metering and leak detection systems")
    if df['internet_connectivity'].mean() < 80:
        recommendations.append("Expand high-speed internet infrastructure")
    if df['crime_rate'].mean() > 5:
        recommendations.append("Implement AI-powered predictive policing and surveillance systems")
    return recommendations

def create_user_urban_plan():
    st.subheader("Create Your Own Urban Plan")
    
    plan = {}
    plan['green_space_increase'] = st.slider("Increase in green space (%)", 0, 100, 20)
    plan['public_transport_expansion'] = st.slider("Public transport expansion (%)", 0, 100, 30)
    plan['renewable_energy_adoption'] = st.slider("Renewable energy adoption (%)", 0, 100, 50)
    plan['smart_city_tech_investment'] = st.slider("Investment in smart city technologies (million $)", 0, 1000, 100)
    plan['affordable_housing_units'] = st.number_input("Number of new affordable housing units", 0, 10000, 1000)
    
    return plan

def simulate_urban_plan(df, plan):
    simulated_df = df.copy()
    
    # Simple simulation logic (this can be made more complex)
    simulated_df['green_space'] *= (1 + plan['green_space_increase'] / 100)
    simulated_df['public_transport_access'] *= (1 + plan['public_transport_expansion'] / 100)
    simulated_df['energy_consumption'] *= (1 - plan['renewable_energy_adoption'] / 200)  # Assuming renewables reduce consumption
    simulated_df['air_quality_index'] *= (1 - plan['renewable_energy_adoption'] / 300)  # Assuming renewables improve air quality
    simulated_df['housing_density'] += plan['affordable_housing_units'] / simulated_df.shape[0]
    
    return simulated_df

def main():
    st.title("Advanced AI-Driven Urban Planning Tool")
    
    data_source = st.radio("Choose data source:", ("Upload File", "Generate Synthetic Data"))
    
    if data_source == "Upload File":
        uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])
        if uploaded_file is not None:
            df = load_data(uploaded_file)
        else:
            df = None
    else:
        num_areas = st.slider("Number of areas to generate:", 50, 500, 100)
        time_periods = st.slider("Number of time periods:", 1, 20, 5)
        df = generate_synthetic_data(num_areas, time_periods)
        st.success(f"Generated synthetic data for {num_areas} areas over {time_periods} time periods.")
        st.markdown(download_csv(df), unsafe_allow_html=True)
    
    if df is not None:
        st.success("Data loaded successfully!")
        
        st.subheader("Data Preview")
        st.write(df.head())
        
        st.subheader("Data Statistics")
        st.write(df.describe())
        
        color_factor = st.selectbox("Choose color factor for visualization", options=df.columns[2:])
        
        visualize_data(df, color_factor)
        analyze_data(df)
        
        focus_areas = [
            "Traffic optimization",
            "Green space expansion",
            "Population density management",
            "Sustainable urban development",
            "Public transportation improvement",
            "Crime reduction",
            "Economic development",
            "Air quality improvement",
            "Healthcare and education enhancement",
            "Smart city initiatives",
            "Water and waste management",
            "Elderly care and accessibility"
        ]
        
        focus_area = st.selectbox("Choose focus area for proposals", options=focus_areas)
        
        if st.button("Generate Comprehensive Urban Development Proposals"):
            proposals = generate_urban_proposal(df, focus_area)
            if proposals:
                export_report(df, proposals)
        
        st.subheader("AI-Powered Urban Planning Insights")
        
        if st.button("Calculate Urban Sustainability Score"):
            sustainability_score = calculate_sustainability_score(df)
            st.write(f"Overall Urban Sustainability Score: {sustainability_score:.2f}/10")
        
        if st.button("Predict Future Urban Trends"):
            future_trends = predict_future_trends(df)
            st.write("Predicted Urban Trends for the Next 5 Time Periods:")
            for feature, prediction in future_trends.items():
                st.write(f"{feature.capitalize()}:")
                st.write(f"  Current value: {prediction['current_value']:.2f}")
                st.write(f"  Predicted values: {', '.join([f'{v:.2f}' for v in prediction['predicted_values']])}")
                st.write(f"  Trend: {prediction['trend']}")
                
                # Visualize prediction
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=list(range(len(prediction['predicted_values']))), 
                                         y=prediction['predicted_values'], 
                                         mode='lines+markers', 
                                         name='Predicted'))
                fig.update_layout(title=f'{feature.capitalize()} Prediction', 
                                  xaxis_title='Time Periods Ahead', 
                                  yaxis_title='Value')
                st.plotly_chart(fig)
        
        if st.button("Recommend Smart City Technologies"):
            smart_city_recommendations = recommend_smart_city_tech(df)
            st.write("Recommended Smart City Technologies:")
            for recommendation in smart_city_recommendations:
                st.write(f"- {recommendation}")
        
        st.subheader("Create and Simulate Your Own Urban Plan")
        user_plan = create_user_urban_plan()
        if st.button("Simulate Urban Plan"):
            simulated_df = simulate_urban_plan(df, user_plan)
            st.write("Simulated Urban Data:")
            st.write(simulated_df.describe())
            
            original_score = calculate_sustainability_score(df)
            simulated_score = calculate_sustainability_score(simulated_df)
            
            st.write(f"Original Sustainability Score: {original_score:.2f}/10")
            st.write(f"Simulated Sustainability Score: {simulated_score:.2f}/10")
            
            if simulated_score > original_score:
                st.success(f"Your plan improved the sustainability score by {simulated_score - original_score:.2f} points!")
            else:
                st.warning(f"Your plan decreased the sustainability score by {original_score - simulated_score:.2f} points. Consider adjusting your strategy.")

if __name__ == "__main__":
    main()
