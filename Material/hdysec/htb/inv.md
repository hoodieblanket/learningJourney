# General usage to assist
- Sending POST REQUEST with `curl -XPOST URLHERE` and getting a response.
- using `echo` and `|` to send a cypher to decode\
   * `echo T1JZRk0tVUZFRFItRVJHSU4tVlJER0ItV1hMTFo= | base64 -d`
   * `echo` in order to produce the string
   * `|` the "pipe" to send the string into the next function
   * `base64 -d` the "d" being decode. removing the `-d` will just default to encoding into base 64
- using `echo` and `|` to send cypher for ROT13 or ROT47
   * For ROT13 `echo "The Quick Brown Fox Jumps Over The Lazy Dog" | tr 'A-Za-z' 'N-ZA-Mn-za-m'`
      * ROT13 is a joke as it is absolutely not secure and a running joke on the net.
      * ROT13 cypher is a rotational jump for each letter, 13 letters down the alphabet.
      * ^ Produces `Gur Dhvpx Oebja Sbk Whzcf Bire Gur Ynml Qbt`  and vice-versa would return to the string.
   * For ROT47 `echo "The Quick Brown Fox Jumps Over The Lazy Dog" | tr '\!-~' 'P-~\!-O"`
      * ^ Produces `%96 "F:4< qC@H? u@I yF>AD ~G6C %96 {2KJ s@8`
      * ROT47 now includes special characters as well.
- Webapp searching using the developer tools for the browser and checking under `Inspector` for interesting url's
   * Under console, just typing the detail such as `makeInviteCode();` will produce results.
   