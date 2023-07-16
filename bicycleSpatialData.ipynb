{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "303d7d78",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n",
      "Map created successfully!\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import folium\n",
    "\n",
    "url = 'https://vancouver.craigslist.org/search/bia'\n",
    "bicycleLinks = []\n",
    "bicycleSpatialData = []\n",
    "\n",
    "# Send a GET request to the URL\n",
    "response = requests.get(url)\n",
    "\n",
    "# Create a BeautifulSoup object\n",
    "soup = BeautifulSoup(response.text, 'html.parser')\n",
    "\n",
    "# Find all the links on the page\n",
    "links = soup.find_all('a', href=lambda href: href and '/bik/' in href)\n",
    "print(links)\n",
    "# Iterate over each link\n",
    "linkcount = 0\n",
    "for link in links:\n",
    "    if linkcount > 100:\n",
    "        break\n",
    "    linkcount += 1\n",
    "    href = link['href']\n",
    "    bicycleLinks.append(href)\n",
    "\n",
    "    # Visit each link to collect spatial data\n",
    "    link_response = requests.get(href)\n",
    "    link_soup = BeautifulSoup(link_response.text, 'html.parser')\n",
    "\n",
    "    # Find the map div and extract latitude and longitude\n",
    "    map_div = link_soup.find('div', id='map')\n",
    "    latitude = float(map_div['data-latitude'])\n",
    "    longitude = float(map_div['data-longitude'])\n",
    "\n",
    "    bicycleSpatialData.append([latitude, longitude])\n",
    "\n",
    "# Create a map of Greater Vancouver\n",
    "vancouver_map = folium.Map(location=[49.2827, -123.1207], zoom_start=10)\n",
    "\n",
    "# Create a feature group for the bicycle spatial data layer\n",
    "bicycle_layer = folium.FeatureGroup(name='Bicycle Spatial Data')\n",
    "\n",
    "# Add markers for each latitude and longitude point in bicycleSpatialData\n",
    "for spatial_data in bicycleSpatialData:\n",
    "    latitude, longitude = spatial_data\n",
    "    marker = folium.Marker(location=[latitude, longitude])\n",
    "    bicycle_layer.add_child(marker)\n",
    "\n",
    "# Add the bicycle spatial data layer to the map\n",
    "vancouver_map.add_child(bicycle_layer)\n",
    "\n",
    "# Add a layer control to toggle the bicycle spatial data layer\n",
    "folium.LayerControl().add_to(vancouver_map)\n",
    "\n",
    "# Save the map to an HTML file\n",
    "vancouver_map.save('vancouver_map.html')\n",
    "\n",
    "print(\"Map created successfully!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f97dea1d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
