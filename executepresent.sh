mkdir encryptedlink
cd encryptedlink
curl https://raw.githubusercontent.com/derpferpmerp/ROT13EncryptedLink/master/encryptedrot13.txt -o encrypted.txt
chmod 777 encrypted.txt
cat encrypted.txt
curl https://raw.githubusercontent.com/derpferpmerp/ROT13EncryptedLink/master/main.py -o decrypter.py
chmod 777 decrypter.py
echo " Working.... "
echo " \n\nExecuting decrypter.py"
python decrypter.py
echo " ! = :"
echo " _ = /"
echo " * = ."
echo " 6 = 0"
echo " 9 = 3"
echo ' Open the Link (Once you\'ve changed those characters) in the browser '