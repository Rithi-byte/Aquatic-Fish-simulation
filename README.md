# 🐠 Real-Time Aquatic Fish Simulation

## Description
This project simulates fish moving in an aquatic environment toward food sources using **Dijkstra's Algorithm** for shortest pathfinding.  
Pollutants are tracked using a **Min-Heap**, and users can manually add pollutants through the web interface.  
The application is built with **Python Flask** (backend) and **HTML/CSS/JavaScript** (frontend).

## Features
- 🐟 Fish intelligently find the nearest food using **Dijkstra’s algorithm**.
- 🍃 Food sources are placed randomly and respawn after consumption.
- ⚡ Fish lose energy over time and regain it by eating food.
- 🛢️ Pollutants like "Oil Spill", "Plastic Waste", etc., are added and tracked using a **Min-Heap** based on severity level.
- 🖱️ Users can manually add different pollutants via the frontend buttons.
- 📈 Real-time updates for fish status, food, and pollution levels every few seconds.

## Technology Stack
- **Backend**: Python, Flask, NetworkX
- **Frontend**: HTML5, CSS3, JavaScript (Fetch API)
- **Others**: Min-Heap (`heapq` module), Dijkstra's algorithm (`networkx.shortest_path`)

## How to Run
1. **Clone the Repository** or extract the provided ZIP file.
2. **Install Dependencies**:
   ```bash
   pip install flask networkx
   ```
3. **Run the Flask Server**:
   ```bash
   python app.py
   ```
4. **Open the Application**:  
   Visit `http://127.0.0.1:5000/` in your browser.

## Project Structure
```
aquatic-simulation/
├── app.py             # Backend server (Flask)
├── templates/
│   └── index.html     # Frontend HTML
├── static/
│   └── (optional for extra JS/CSS files)
├── README.md          # Project Instructions
```

## Screenshots
*(Optional: Add screenshots after running the project)*

- **Fish Movement Simulation**
- **Real-time Pollutant Updates**
- **Manual Pollutant Addition via Buttons**

## Requirements
Create a `requirements.txt` file:
```
Flask
networkx
```
Then install:
```bash
pip install -r requirements.txt
```

## Author
Made with ❤️ for an aquatic environment simulation project.
