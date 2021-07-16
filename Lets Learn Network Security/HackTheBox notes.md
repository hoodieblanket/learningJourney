# Learning Vulnerabilities <!-- omit in toc -->

---
## Table of Contents

---

- [Table of Contents](#table-of-contents)
- [Using `curl` to post and receive response from webserver](#using-curl-to-post-and-receive-response-from-webserver)
- [For Base64 encoding](#for-base64-encoding)
  - [Using `echo` and pipe `|` to decode `base64` encoding](#using-echo-and-pipe--to-decode-base64-encoding)
- [For ROT13 encoding](#for-rot13-encoding)
  - [using `echo` and pipe `|` to decode ROT13 or ROT47](#using-echo-and-pipe--to-decode-rot13-or-rot47)
- [For ROT47 encoding](#for-rot47-encoding)
- [Webapp searching](#webapp-searching)

---
## Using `curl` to post and receive response from webserver

---

| Option                | Description                                      |
| :-------------------- | :----------------------------------------------- |
| `curl -XPOST URLHERE` | Sending POST REQUEST with and getting a response |

[Back to Top](#table-of-contents)

---
## For Base64 encoding

---
Modifiers

| Option | Description                                                   |
| :----- | :------------------------------------------------------------ |
| `-d`   | decode rather than encode the data                            |
| `-i`   | ignore non-alphabetical characters and thereby remove garbage |

[Back to Top](#table-of-contents)

---
### Using `echo` and pipe `|` to decode `base64` encoding

---

| Option      | Description                                                                          |
| :---------- | :----------------------------------------------------------------------------------- |
| `echo`      | in order to produce the string\                                                      |
| `base64 -d` | the "d" being decode. removing the `-d` will just default to *encoding* into base 64 |
| &#124;      | the "pipe" to send the string into the next function                                 |

`echo T1JZRk0tVUZFRFItRVJHSU4tVlJER0ItV1hMTFo= | base64 -d` - using `echo` and `|` to send a cypher to decode

[Back to Top](#table-of-contents)

---
## For ROT13 encoding

---

ROT13 is a bit of a running joke due to the simplicity of the encoding and resulting algorithm required to decode it. Thus anything protected by ROT13 is not really protected at all

ROT13 cypher is a rotational jump for each letter, 13 letters down the alphabet.

`echo "The Quick Brown Fox Jumps Over The Lazy Dog" | tr 'A-Za-z' 'N-ZA-Mn-za-m'` \
Produces for `Gur Dhvpx Oebja Sbk Whzcf Bire Gur Ynml Qbt`  and vice-versa would return to the string

[Back to Top](#table-of-contents)

---
### using `echo` and pipe `|` to decode ROT13 or ROT47

---

`echo` - in order to produce the string\
`|` - the "pipe" to send the string into the next function

[Back to Top](#table-of-contents)

---
## For ROT47 encoding

---

ROT47 includes special character as well now which means the length of the characters available is large but still similar level of security

`echo "The Quick Brown Fox Jumps Over The Lazy Dog" | tr '\!-~' 'P-~\!-O"` \
Produces `%96 "F:4< qC@H? u@I yF>AD ~G6C %96 {2KJ s@8`

[Back to Top](#table-of-contents)

---
## Webapp searching

---

Webapp searching using the developer tools for the browser and checking under `Inspector` for interesting urls

- This may lead to urls to gather further information to gather data in order to plan ahead
- Potential webpages that shouldn't be accessible creating a vulnerability
- For example, having an invite-only website that would not usually be accessbile however referring under console, just typing the detail such as `makeInviteCode();` will produce results and show possible links and additional information to potentially create your own invite code

[Back to Top](#table-of-contents)

---