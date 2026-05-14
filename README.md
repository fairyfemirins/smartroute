# SmartRoute - Live Traffic Route Viewer

A web-based tool for viewing live traffic camera feeds along your route. Overlays real-time traffic conditions on a map to help users avoid congestion and accidents.

## Features (MVP)
- **Route Input:** Enter start and end locations.
- **Traffic Camera Overlay:** Fetch and display live traffic camera feeds along the route.
- **Real-Time Conditions:** Show congestion, accidents, and road closures.
- **Alternative Routes:** Suggest detours based on live traffic data.

## Technical Architecture

### Backend
- **Framework:** Flask (Python)
- **APIs:** Public traffic camera feeds (e.g., state DOT APIs)
- **Routing:** OpenStreetMap or Google Maps API

### Frontend
- **Framework:** Bootstrap (HTML/CSS/JavaScript) + Leaflet.js
- **Features:**
  - Interactive map with route overlay
  - Traffic camera markers with live feeds
  - Responsive design (mobile/desktop)

### Data Flow
1. User enters start and end locations.
2. Backend fetches route coordinates from a mapping API.
3. Backend fetches traffic camera feeds along the route.
4. Frontend displays the route and camera feeds on a map.

## Roadmap
- **Accident Detection:** Use AI to detect accidents from camera feeds.
- **Weather Overlay:** Integrate weather data for route planning.
- **Historical Data:** Show traffic patterns for specific times/days.
- **Mobile App:** React Native for iOS/Android.

## License
MIT