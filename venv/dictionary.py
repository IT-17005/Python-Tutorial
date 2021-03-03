student = {
    101 : "RUHAN",
    "102" : "Abdullah",
    "103" : "sultan",
    "104" : "ridom",
}
print(student.get("102"))
print(student.get("103"))
print(student.get(101))
print(student.get("106","Not a valid key."))