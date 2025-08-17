import pickle
import streamlit as st
import pandas as pd

# ----------------- Helper Functions -----------------


def format_runtime(runtime):
    """Format runtime from minutes to hours and minutes"""
    if pd.isna(runtime) or runtime == '' or runtime == 0:
        return "Unknown"
    try:
        runtime_num = float(runtime)
        if runtime_num <= 0:
            return "Unknown"
        hours = int(runtime_num // 60)
        minutes = int(runtime_num % 60)
        if hours > 0:
            return f"{hours}h {minutes}m"
        else:
            return f"{minutes}m"
    except (ValueError, TypeError):
        return "Unknown"

def format_date(date_str):
    """Format release date"""
    if pd.isna(date_str) or date_str == '':
        return "Unknown"
    try:
        return pd.to_datetime(date_str).strftime("%B %d, %Y")
    except:
        return str(date_str)

def truncate_text(text, max_length=150):
    """Truncate text to specified length"""
    if pd.isna(text) or text == '':
        return "No description available"
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."

def safe_get(movie, key, default="N/A"):
    """Safely get value from movie dictionary"""
    try:
        value = movie.get(key, default)
        if pd.isna(value) or value == '':
            return default
        return value
    except:
        return default

# ----------------- Recommendation Functions -----------------
def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movies = []
        for i in distances[1:6]:
            recommended_movies.append(movies.iloc[i[0]])
        return recommended_movies
    except Exception as e:
        st.error(f"Error in recommendation: {str(e)}")
        return []



# ----------------- Streamlit UI -----------------
st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
    layout="wide"
)

# Custom CSS for clean styling
st.markdown("""
<style>
    .movie-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        margin: 15px 0;
        color: white;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    .movie-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0,0,0,0.2);
    }
    .movie-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 15px;
        color: #ffffff;
    }
    .movie-info {
        background: rgba(255,255,255,0.1);
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .info-badge {
        background: #ffd700;
        color: #000;
        padding: 5px 10px;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
        margin: 5px 5px 5px 0;
    }
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 25px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    .stats-card {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 10px 0;
    }
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 20px;
        color: white;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

# Main Header
st.markdown("""
<div class="main-header">
    <h1>🎬 Movie Recommender System</h1>
    <p>Discover your next favorite movie with AI-powered recommendations</p>
</div>
""", unsafe_allow_html=True)

# Load data with error handling
try:
    movies = pickle.load(open('artifacts/movie_list.pkl','rb'))
    similarity = pickle.load(open('artifacts/similarity.pkl','rb'))
    
    # Show project info in sidebar
    st.sidebar.markdown("### 🎬 About This Project")
    st.sidebar.markdown("""
    **Movie Recommender System** is an AI-powered application that helps you discover your next favorite movie.
    
    **Features:**
    • 🎯 **Movie Similarity**: Find movies similar to your favorites
    • 🤖 **ML-Powered**: Uses machine learning for recommendations
    • 📱 **User-Friendly**: Clean, modern interface
    • 📊 **Rich Data**: Runtime, overview, and release dates
    """)
    
    st.sidebar.markdown("---")
    
    # Quick stats
    st.sidebar.markdown("### 📊 Quick Stats")
    st.sidebar.metric("Total Movies", f"{len(movies):,}")
    
    # Check available columns safely
    has_runtime = 'runtime' in movies.columns
    has_overview = 'overview' in movies.columns
    has_release_date = 'release_date' in movies.columns
    
    # Show data quality info
    st.sidebar.markdown("### 🔍 Data Quality")
    if has_runtime:
        st.sidebar.success("✅ Runtime data available")
    else:
        st.sidebar.warning("⚠️ No runtime data")
        
    if has_overview:
        st.sidebar.success("✅ Overview data available")
    else:
        st.sidebar.warning("⚠️ No overview data")
        
    if has_release_date:
        st.sidebar.success("✅ Release date data available")
    else:
        st.sidebar.warning("⚠️ No release date data")
    
    st.sidebar.markdown("---")
    
    # How to use
    st.sidebar.markdown("### 💡 How to Use")
    st.sidebar.markdown("""
    1. **Select a movie** from the dropdown
    2. **Click 'Get Recommendations'**
    3. **Discover similar movies** based on ML analysis
    4. **Explore movie details** in beautiful cards
    """)
    
    st.sidebar.markdown("---")
    
    # Project info
    st.sidebar.markdown("### 🚀 Project Info")
    st.sidebar.markdown("""
    **Built with:**
    • Python + Streamlit
    • Machine Learning
    • Pandas + Pickle
    • Beautiful UI/UX
    
    **Data Source:**
    • TMDB Movie Database
    • 5000+ movies
    • Rich metadata
    """)
        
except Exception as e:
    st.error(f"❌ Error loading data: {str(e)}")
    st.stop()

# Statistics Dashboard
st.subheader("📊 Quick Statistics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="stats-card">
        <h3>🎬 Total Movies</h3>
        <h2>{len(movies):,}</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    if has_runtime:
        try:
            avg_runtime = movies['runtime'].mean()
            st.markdown(f"""
            <div class="stats-card">
                <h3>⏱️ Avg Runtime</h3>
                <h2>{int(avg_runtime) if not pd.isna(avg_runtime) else 'N/A'}m</h2>
            </div>
            """, unsafe_allow_html=True)
        except:
            st.markdown(f"""
            <div class="stats-card">
                <h3>⏱️ Avg Runtime</h3>
                <h2>N/A</h2>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="stats-card">
            <h3>🚀 Ready to Go!</h3>
            <h2>Start Exploring</h2>
        </div>
        """, unsafe_allow_html=True)

with col3:
    if has_overview:
        st.markdown(f"""
        <div class="stats-card">
            <h3>📝 Overview</h3>
            <h2>Available</h2>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="stats-card">
            <h3>💡 Smart AI</h3>
            <h2>ML Powered</h2>
        </div>
        """, unsafe_allow_html=True)

with col4:
    if has_release_date:
        st.markdown(f"""
        <div class="stats-card">
            <h3>📅 Release Date</h3>
            <h2>Available</h2>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="stats-card">
            <h3>🎯 Get Started</h3>
            <h2>Pick a Movie</h2>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# Add engaging content section
st.markdown("""
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; margin: 20px 0;">
    <h2>🎬 Ready to Discover Your Next Favorite Movie?</h2>
    <p style="font-size: 18px; margin: 15px 0;">Our AI-powered system analyzes thousands of movies to find the perfect match for your taste!</p>
    <p style="font-size: 16px; opacity: 0.9;">✨ Just select a movie you love and let the magic happen ✨</p>
</div>
""", unsafe_allow_html=True)

# Fun Facts Section
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%); padding: 20px; border-radius: 15px; color: white; text-align: center;">
        <h3>🤖 How It Works</h3>
        <p>Our ML algorithm analyzes movie features like plot, cast, genre, and more to find similar movies you'll love!</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #4ecdc4 0%, #44a08d 100%); padding: 20px; border-radius: 15px; color: white; text-align: center;">
        <h3>💡 Pro Tips</h3>
        <p>• Try different types of movies<br>• Explore various genres<br>• Rate the recommendations<br>• Share with friends!</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Main Recommendation Section
st.subheader("🎯 Get Movie Recommendations")

# Movie selection
try:
    st.subheader("🎯 Movie Similarity Recommendations")
    
    movie_list = movies['title'].values
    selected_movie = st.selectbox("🔎 Select a movie", movie_list, key="movie_select")
    
    if st.button("🚀 Get Recommendations", key="rec_btn"):
        try:
            with st.spinner("🎬 Finding similar movies..."):
                recs = recommend(selected_movie)
            
            if recs:
                st.success(f"✨ Here are movies similar to **{selected_movie}**")
                st.markdown("---")
                
                # Display recommendations
                for idx, movie in enumerate(recs, 1):
                    st.markdown(f"""
                    <div class="movie-card">
                        <div class="movie-title">#{idx} {safe_get(movie, 'title', 'Unknown Title')}</div>
                        <div class="movie-info">
                            <p><strong>📅 Release Date:</strong> {format_date(safe_get(movie, 'release_date', 'N/A'))}</p>
                            <p><strong>⏱️ Runtime:</strong> {format_runtime(safe_get(movie, 'runtime', 'N/A'))}</p>
                            <p><strong>📝 Overview:</strong> {truncate_text(safe_get(movie, 'overview', 'N/A'))}</p>
                            <div style="margin-top: 15px;">
                                <span class="info-badge">🎬 Movie #{idx}</span>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.markdown("---")
            else:
                st.warning("No recommendations found. Please try another movie.")
                
        except Exception as e:
            st.error(f"❌ Error getting recommendations: {str(e)}")
            
except Exception as e:
    st.error(f"❌ Error loading movie list: {str(e)}")

# Footer
st.markdown("---")

# Motivational section
st.markdown("""
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 25px; border-radius: 15px; text-align: center; margin: 20px 0; border: 2px solid #ddd;">
    <h3 style="color: white; margin-bottom: 15px; font-size: 24px;">🌟 Why Choose Our Recommender?</h3>
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 15px;">
        <div style="background: white; padding: 15px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <h4 style="color: #667eea; margin: 0; font-size: 20px;">🎯</h4>
            <p style="margin: 5px 0; font-size: 14px; color: #333; font-weight: bold;">Accurate</p>
        </div>
        <div style="background: white; padding: 15px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <h4 style="color: #667eea; margin: 0; font-size: 20px;">⚡</h4>
            <p style="margin: 5px 0; font-size: 14px; color: #333; font-weight: bold;">Fast</p>
        </div>
        <div style="background: white; padding: 15px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <h4 style="color: #667eea; margin: 0; font-size: 20px;">🤖</h4>
            <p style="margin: 5px 0; font-size: 14px; color: #333; font-weight: bold;">Smart</p>
        </div>
        <div style="background: white; padding: 15px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <h4 style="color: #667eea; margin: 0; font-size: 20px;">💎</h4>
            <p style="margin: 5px 0; font-size: 14px; color: #333; font-weight: bold;">Reliable</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("🎬 *Powered by Machine Learning & Rich Movie Data*")
st.markdown("💡 *Simple • Clean • Working*")