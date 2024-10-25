import streamlit as st
import streamlit.components.v1 as components

# Set the page configuration to wide mode
st.set_page_config(layout="wide")

# List of symbols to display
symbols = [
    "PEPPERSTONE:VIX",
    "COINBASE:BTCUSD",
    "FOREXCOM:SPXUSD",
    "FOREXCOM:NSXUSD",
    "FOREXCOM:DJI",
    "FOREXCOM:AUS200",
    "FOREXCOM:JP225",
    "FOREXCOM:HK50",
    "FOREXCOM:UKXGBP"
]

# Generate HTML for each TradingView single quote widget
tradingview_widgets = '<div style="display: flex; flex-wrap: wrap; justify-content: center;">'
for symbol in symbols:
    tradingview_widgets += f"""
    <div class="tradingview-widget-container" style="flex: 1 0 30%; margin: 10px; max-width: 300px;">
      <div class="tradingview-widget-container__widget"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
      {{
      "symbol": "{symbol}",
      "width": "100%",
      "isTransparent": false,
      "colorTheme": "light",
      "locale": "en"
      }}
      </script>
    </div>
    """
tradingview_widgets += '</div>'

# Add JavaScript to remove the copyright link
tradingview_widgets += """
<script>
  window.onload = function() {
    var copyrightLink = document.querySelector('a.label__link-dzbd7lyV');
    if (copyrightLink) {
      copyrightLink.remove();
    }
  };
</script>
"""

# Render the TradingView widgets
components.html(tradingview_widgets, height=600)  # Adjust height as needed