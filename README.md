# 🎬 Movie Recommender System Using Machine Learning

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An intelligent, AI-powered movie recommendation system that helps users discover their next favorite movie using machine learning algorithms.

## ✨ Features

- 🎯 **Smart Recommendations**: ML-powered content-based filtering
- 🎬 **Rich Movie Database**: 5000+ movies with comprehensive metadata
- 🎨 **Beautiful UI**: Modern, responsive interface built with Streamlit
- ⚡ **Fast Performance**: Instant recommendations in under 1 second
- 📱 **User-Friendly**: Intuitive design with hover effects and animations
- 🔍 **Rich Information**: Detailed movie data including runtime, release dates, and overviews

## 🚀 Live Demo

**Try the app:** [Streamlit Cloud Deployment](https://your-app-name.streamlit.app)

## 🛠️ Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Backend**: Python 3.7+
- **Machine Learning**: Content-based filtering with cosine similarity
- **Data Processing**: Pandas, NumPy
- **Data Storage**: Pickle files, CSV
- **Styling**: Custom CSS with gradients and animations

## 📊 Project Structure

```
Movie-Recommender-System-Using-Machine-Learning/
├── app.py                          # Main Streamlit application
├── requirements.txt                 # Python dependencies
├── README.md                       # Project documentation
├── LICENSE                         # MIT License
├── artifacts/                      # ML model files
│   ├── movie_list.pkl             # Processed movie data
│   └── similarity.pkl             # Pre-computed similarity matrix
├── data/                          # Raw data files
│   └── tmdb_5000_movies.csv      # TMDB movie dataset
└── src/                           # Source code (if any)
```

## 🎯 How It Works

1. **Data Processing**: Movie metadata is extracted and processed from TMDB dataset
2. **Feature Engineering**: Text features are vectorized and normalized
3. **Similarity Calculation**: Cosine similarity is computed between all movie pairs
4. **Recommendation Generation**: Top 5 most similar movies are returned based on user selection
5. **User Interface**: Beautiful cards display movie information with rich formatting

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/Movie-Recommender-System-Using-Machine-Learning.git
cd Movie-Recommender-System-Using-Machine-Learning
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📱 Usage

1. **Select a Movie**: Choose from the dropdown of 5000+ movies
2. **Get Recommendations**: Click "Get Recommendations" button
3. **Explore Results**: View 5 similar movies with detailed information
4. **Discover More**: Each movie card shows runtime, release date, and overview

## 🎨 UI Features

- **Gradient Backgrounds**: Beautiful blue-to-purple gradients
- **Hover Effects**: Interactive movie cards with smooth animations
- **Responsive Design**: Works perfectly on all device sizes
- **Information Cards**: Clean, readable movie presentations
- **Sidebar Navigation**: Project information and usage guide

## 🔧 Customization

### Adding New Movies
1. Update the CSV file in the `data/` folder
2. Re-run the preprocessing script
3. Update the pickle files

### Modifying the UI
- Edit CSS styles in the `app.py` file
- Modify the Streamlit components
- Add new features and sections

## 📈 Performance Metrics

- **Recommendation Speed**: < 1 second
- **Database Size**: 5000+ movies
- **Accuracy**: High-quality similarity matching
- **Scalability**: Easy to add more movies and features

## 🚀 Future Enhancements

- [ ] User ratings and feedback system
- [ ] Collaborative filtering algorithms
- [ ] Genre-based filtering
- [ ] Movie trailers and poster images
- [ ] Mobile app version
- [ ] User authentication and profiles
- [ ] Advanced ML models (neural networks)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **TMDB**: For providing the comprehensive movie dataset
- **Streamlit**: For the amazing web framework
- **Open Source Community**: For various Python libraries and tools

## 📞 Contact

**Project Link**: [https://github.com/your-username/Movie-Recommender-System-Using-Machine-Learning](https://github.com/your-username/Movie-Recommender-System-Using-Machine-Learning)

---

⭐ **Star this repository if you found it helpful!**
