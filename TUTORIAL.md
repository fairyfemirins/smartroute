# SmartRoute: Reproducible Tutorial

## 1. Prerequisites
- Python 3.8+
- Git

---

## 2. Setup
```bash
# Clone the repository
git clone https://github.com/fairyfemirins/smartroute.git
cd smartroute

# Set up a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 3. Run the Application
```bash
# Start the Flask development server
python3 app.py
```

Open your browser and navigate to:
```
http://127.0.0.1:5000
```

---

## 4. Test the Features

### 4.1 Enter a Route
1. Enter a start location (e.g., "San Francisco").
2. Enter an end location (e.g., "New York").
3. Click "Search Route".

Expected output:
- A map with a blue route line from start to end.
- Markers for traffic cameras along the route.
- Click on a marker to view a mock traffic camera feed.

---

## 5. Extend the Application
- **Add Real Traffic Data:** Replace mock camera feeds with real API calls (e.g., state DOT APIs).
- **Add Accident Detection:** Use AI to analyze camera feeds for accidents.
- **Deploy:** Host on Render, Vercel, or AWS.

---

## 6. License
MIT