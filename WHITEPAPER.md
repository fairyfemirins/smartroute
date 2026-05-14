# SmartRoute: Design and Rationale

## 1. Introduction
Real-time traffic updates are critical for commuters, yet existing solutions rely on **predictive models** rather than live data. SmartRoute addresses this gap by overlaying **live traffic camera feeds** on a map, providing users with **actual traffic conditions** along their route.

---

## 2. Design Decisions

### 2.1 Technology Stack
- **Backend:** Flask (Python) for simplicity and rapid development.
- **Frontend:** Bootstrap (HTML/CSS/JavaScript) + Leaflet.js for interactive maps.
- **Mapping API:** OpenStreetMap or Google Maps API for routing.
- **Traffic Data:** Public traffic camera APIs (e.g., state DOT feeds).

**Rationale:**
- Flask is lightweight and easy to extend.
- Leaflet.js provides interactive maps with minimal overhead.
- Public traffic camera APIs offer free, real-time data.

### 2.2 Core Features
1. **Route Input:** Users enter start and end locations.
2. **Traffic Camera Overlay:** Fetch and display live camera feeds along the route.
3. **Real-Time Conditions:** Show congestion, accidents, and road closures.
4. **Alternative Routes:** Suggest detours based on live traffic data.

**Rationale:**
- Focus on **core functionality** first (MVP).
- Extensibility for future features (e.g., accident detection, weather overlays).

### 2.3 Challenges
- **Data Availability:** Traffic camera feeds vary by location and may require API keys.
- **Scalability:** Handle large volumes of users and camera feeds.
- **Real-Time Updates:** Ensure camera feeds are refreshed frequently.

---

## 3. Future Work
- **Accident Detection:** Use AI to detect accidents from camera feeds.
- **Weather Overlay:** Integrate weather data for route planning.
- **Historical Data:** Show traffic patterns for specific times/days.
- **Mobile App:** React Native for iOS/Android.

---

## 4. Conclusion
This project demonstrates how **live traffic camera feeds** can enhance route planning. By focusing on **real-time data, simplicity, and extensibility**, it provides a foundation for future enhancements.

## License
MIT