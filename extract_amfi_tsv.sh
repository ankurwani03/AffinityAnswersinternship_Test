NAV_URL="https://www.amfiindia.com/spages/NAVAll.txt"

OUTPUT_FILE="amfi_data.tsv"

echo "Downloading AMFI NAV data..."
curl -s $NAV_URL -o NAVAll.txt

if [[ ! -f "NAVAll.txt" ]]; then
  echo " Failed to download NAV data!"
  exit 1
fi
header=$(head -n 1 NAVAll.txt)

echo " Extracting Scheme Name and Asset Value (NAV)..."

awk -F'|' '
BEGIN { 
    OFS="\t";  
    print "Scheme Name", "Net Asset Value";  
}
/^[0-9]/ {
    scheme=$4;  
    nav=$5;    
    if (scheme != "" && nav != "") {
        print scheme, nav;  
    }
}
' NAVAll.txt > $OUTPUT_FILE

if [[ -f "$OUTPUT_FILE" ]]; then
  echo " Scheme Name and Asset Value (NAV) saved to $OUTPUT_FILE"
else
  echo " Error saving the data to $OUTPUT_FILE"
fi
