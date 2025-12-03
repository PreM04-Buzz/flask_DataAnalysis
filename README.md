# US Immigration Data Analysis Dashboard

This project is a Flask-based data analysis dashboard built to explore, visualize, and manage US immigration statistics. It converts raw CSV data into an interactive dashboard with sortable tables, search functionality, CRUD operations, and multiple chart visualizations. The system uses a clean blue-themed interface along with Chart.js for displaying trends.

## Features

### Data Management (CRUD)
- Add new immigration records
- Edit existing records
- Delete unwanted or incorrect entries
- Automatic database creation from CSV when the app first runs

### Interactive Table Tools
- Live search bar to filter results instantly
- Clickable column headers for ascending or descending sorting
- Clean border styling and table layout
- Fully responsive design

### Data Filtering and Analysis
- Filter results based on year ranges
- Compare trends across data categories
- Multi-chart dashboard for deeper insight

### Visualizations (Chart.js)
- Line charts for trends such as Immigrants, Refugees, Apprehensions
- Bar charts for comparisons such as Removals vs Returns
- Dynamic axes and hover-based chart interactions
- Organized multi-chart dashboard layout

### User Interface
- Clean blue-themed design
- Back button navigation on all pages except home
- Logo header
- Consistent and readable layout

## Installation Instructions

1. Download or clone the project repository.
2. Create a virtual environment:
   macOS: python3 -m venv venv
          source venv/bin/activate
   Windows: python -m venv venv
            venv\Scripts\activate
3. Install required packages:
   pip install -r requirements.txt
4. Add your data file named: immigration.csv
5. Run the application:
   macOS: python3 app.py
   Windows: python app.py
6. Open in browser: http://127.0.0.1:5000/

## Technologies Used

Flask  
SQLite  
Pandas  
Chart.js  
HTML, CSS, JavaScript  
Python 3  

## Purpose

This project helps users analyze US immigration trends through interactive visualizations and clean data management tools. It is designed for students, developers, and analysts who need a simple but powerful data analysis interface.

## Future Enhancements

- Export filtered results as CSV
- Add pagination for large datasets
- Add user authentication
- Add dark mode
- Add AI-based data insights

## License

This project is open-source and free for academic and personal use.
