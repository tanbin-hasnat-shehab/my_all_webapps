mkdir -p ~/.streamlt/
echo "
[server]\n
headless = true\n
enableCORS=false\n
port = $PORT \n
\n
" > ~/.streamlit/config.toml