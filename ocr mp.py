import easyocr
import re
import pandas as pd
import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    popup.geometry("300x200")
    label = ttk.Label(popup, text="Average Temperature:", font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Got It", command=popup.destroy)
    B1.pack()
    popup.mainloop()


# Initialize EasyOCR with the desired languages
reader = easyocr.Reader(['en'])

# Load the image
image_path = image_path = "C:\\Users\\vmyog\\OneDrive\\Desktop\\national hackaton\\WhatsApp Image 2024-09-23 at 21.24.55_c12c9329.jpg"


# Perform OCR on the image
results = reader.readtext(image_path)

# Initialize lists to store extracted text and numeric values
extracted_text = []
extracted_numeric_values = []

# Iterate through the OCR results
for result in results:
    text = result[1]

    # Extract numeric values using regular expressions
    numeric_values = re.findall(r'-?\d+(\.\d*)?', text)

    # Add the text to the list of extracted text
    extracted_text.append(text)

    # Add the numeric values to the list of extracted numeric values
    extracted_numeric_values.extend(numeric_values)

# extracted_numeric_values = [float(num) for num in extracted_numeric_values if num.replace('.', '', 1).isdigit()]


for i in range(len(extracted_text)):
    if extracted_text[i].isdigit():
        extracted_text[i] = int(extracted_text[i])

data = extracted_text

if 40160 in data:
    data.remove(40160)
print(data)
temp = 0;
print(len(data))
for i in range(0, len(data)):
    strtdata = str(data[i])
    if len(str(data[i])) == 2 and strtdata[0] == 'T':
        print("Temperature :", data[i + 1])
        temp += float(data[i + 1])
print("Average Temperature : ", temp / 2)
popupmsg(temp / 2)

# key_words = ['HR', 'T1']
# result_dict = {}
# flag = False
# for i,temp in enumerate(data):
#     if(temp in key_words):
#         for num in data[i:]:
#             if str(num).isnumeric():
#                 result_dict[T1] = [num]
#                 break
# print(result_dict)

key_words = ['RESP', 'T1']
result_dict = {kw: [] for kw in key_words}
current_key = None
for num in extracted_numeric_values:
    if current_key is not None:
        result_dict[current_key].append(num)
    elif num in key_words:
        current_key = num

print(result_dict)
# df = pd.DataFrame(result_dict)
# df.to_csv('Data2.csv',index=False)
# df = pd.read_csv('./Data2.csv')
# df = df.append(result_dict,ignore_index=True)

# print(df)
# df.to_csv("Data2.csv")