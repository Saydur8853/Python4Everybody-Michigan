# 6.5 Write code using find() and string slicing (see section 6.10) to extract
# the number at the end of the line below. Convert the extracted value to a
# floating point number and print it out.


text = "X-DSPAM-Confidence:    0.8475";
start = text.find('0')
end = text.find('5')
finish = text[start:end+1]
final_value = float(finish)
print (final_value)
