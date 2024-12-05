import csv
import os
import requests

# Parameters for the image cutout service
scale = 0.2  # Image scale in arcseconds/pixel
width = 64  # Width of the image in pixels
height = 64  # Height of the image in pixels
base_url = "https://skyserver.sdss.org/dr18/SkyServerWS/ImgCutout/getjpeg"

# Csv file downloaded from syserver sdss using sql queries
csv_file = "QSO200000.csv"
image_folder = "images"  


os.makedirs(image_folder, exist_ok=True)


ra_column = 3   
dec_column = 4  
image_column_name = "Image File Path"  
l=0

rows = []
with open(csv_file, "r", newline="") as infile:
    reader = csv.reader(infile)
    header = next(reader)

    
    if image_column_name not in header:
        header.append(image_column_name)

    
    for row in reader:
        try:
            
            ra = float(row[ra_column])
            dec = float(row[dec_column])

            
            url = f"{base_url}?ra={ra}&dec={dec}&scale={scale}&width={width}&height={height}"

            
            response = requests.get(url)
            if response.status_code == 200:
                
                filename = os.path.join(image_folder, f"sdss_image_{ra}_{dec}.jpg")
                with open(filename, "wb") as file:
                    file.write(response.content)
                print(l,f"Downloaded: {filename}")
                l=l+1

                
                if len(row) < len(header):
                    row.append(filename)
                else:
                    row[-1] = filename  
            else:
                print(f"Failed to download image for RA: {ra}, Dec: {dec} (HTTP {response.status_code})")
                if len(row) < len(header):
                    row.append("Download Failed")
                else:
                    row[-1] = "Download Failed"
        except Exception as e:
            print(f"Error processing RA: {ra}, Dec: {dec} - {e}")
            if len(row) < len(header):
                row.append("Error")
            else:
                row[-1] = "Error"

        
        rows.append(row)


with open(csv_file, "w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(rows)

print(f"Processing complete. Images saved in the '{image_folder}' folder, and the CSV file has been updated.")
