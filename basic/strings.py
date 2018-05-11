"Isn'\t she said"
print("Isn'\t she said");
print(r"Isn'\t she said"); #r will not interpret escape characters
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""");#add \ to multi line string to avoid new line

print(3 * 'un' + 'inm');

print('harish' 'sutar'); #concatenate two string literals directly

word = 'python';
print(word + 'thon');
print(word);

print(word[0:2]);
print(word[:5]);
print(word[2:]);
print(word[-1:]);
print(word[:-1]);
print(word[:6])
print(word[-6:])
print(len(word));
