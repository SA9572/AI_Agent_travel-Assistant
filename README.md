# Agentic Travel Assistant

An intelligent AI-powered travel planning assistant built with LangChain and Groq. This application helps users plan their trips by providing flight recommendations, hotel suggestions, destination information, weather forecasts, and budget estimates.

## Features

- **✈️ Flight Search**: Find and compare flight options for your travel dates
- **🏨 Hotel Recommendations**: Get personalized hotel suggestions based on preferences
- **🌍 Destination Planning**: Discover attractions and places to visit
- **🌤️ Weather Forecasts**: Check weather conditions for your destination
- **💰 Budget Estimation**: Calculate estimated costs for your entire trip
- **🤖 AI-Powered Agent**: Intelligent agent that understands natural language queries and leverages multiple tools

## Tech Stack

- **Backend**: Flask (Python)
- **AI/LLM**: LangChain + Groq API
- **Frontend**: HTML, CSS, JavaScript
- **Dependencies**: See `requirements.txt`

## Project Structure

```
agentic-travel-assistant/
├── agent/                 # AI Agent logic
│   ├── travel_agent.py   # Main agent creation and setup
│   ├── prompts.py        # System prompts and instructions
│   └── __init__.py
├── app/                   # Application configuration
│   ├── config.py
│   └── data/             # Sample data files
│       ├── flights.json
│       ├── hotels.json
│       └── places.json
├── tools/                 # Tool implementations
│   ├── flight_tool.py
│   ├── hotel_tool.py
│   ├── places_tool.py
│   ├── weather_tool.py
│   └── budget_tool.py
├── web/                   # Frontend assets
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── script.js
│       └── style.css
├── main.py               # Flask application entry point
├── requirements.txt      # Python dependencies
└── render.yaml          # Deployment configuration
```

## Installation

### Prerequisites
- Python 3.8+
- Groq API Key (get one at [console.groq.com](https://console.groq.com))

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/SA9572/AI_Agent_travel-Assistant.git
   cd agentic-travel-assistant
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   # Create a .env file in the root directory
   echo GROQ_API_KEY=your_api_key_here > .env
   ```

## Usage

### Run the Application

```bash
python main.py
```

The application will start on `http://localhost:5000`

### API Endpoints

#### `GET /`
- **Description**: Serves the web interface
- **Response**: HTML page

#### `POST /plan`
- **Description**: Submit a travel planning query
- **Request Body**:
  ```json
  {
    "query": "I need to plan a trip to Paris for 5 days with a budget of $2000"
  }
  ```
- **Response**:
  ```json
  {
    "result": "AI-generated travel plan..."
  }
  ```

### Example Queries

- "Find flights from New York to London for next week"
- "Recommend hotels in Tokyo within $150 per night"
- "What are the best attractions in Barcelona?"
- "What's the weather like in Sydney?"
- "Plan a 7-day trip to Italy with a $3000 budget"

## Tools

### Flight Tool
Searches for available flights based on origin, destination, and dates.

### Hotel Tool
Recommends hotels based on location, price range, and preferences.

### Places Tool
Provides information about attractions and places to visit in destinations.

### Weather Tool
Fetches weather forecasts for specified locations.

### Budget Tool
Calculates estimated trip costs including flights, accommodation, and activities.

## Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

**Note**: The `.env` file is ignored in git for security purposes. See `.gitignore` for details.

## Deployment

The project includes a `render.yaml` configuration file for easy deployment to Render:

1. Push your code to GitHub
2. Connect your repository to Render
3. The app will automatically deploy using the configuration in `render.yaml`

## Development

### Running in Debug Mode

The application runs in debug mode by default, which enables:
- Auto-reloading on code changes
- Detailed error messages
- Interactive debugger

### Project Architecture

The agent uses a ReAct (Reasoning + Acting) pattern:
1. User submits a natural language query
2. LLM analyzes the query and decides which tools to use
3. Tools execute and return results
4. LLM synthesizes the results into a comprehensive response

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Support

For issues and questions, please open an issue on the [GitHub repository](https://github.com/SA9572/AI_Agent_travel-Assistant/issues).

## Author

SA9572