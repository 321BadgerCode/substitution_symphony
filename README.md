<p align="center">
	<img src="./asset/logo.png" alt="Substitution Symphony Logo" width="200" height="200">
</p>

<h1 align="center">Substitution Symphony</h1>

<p align="center">
	<strong>Encrypt and decipher messages!</strong>
</p>

## 🚀 Overview

**Substitution Symphony** is a simple program that allows you to encrypt and decipher messages using a substitution cipher. `./encrypt.py` encrypts a given message to the emoji substitution ciphertext. `./main.py`, on the other hand, uses cryptanalysis methods to decipher a emoji ciphertext message by displaying it in the predicted plaintext output.

## 🎨 Features

- **Encryption**: Encrypt a given message to the emoji substitution ciphertext.
- **Decryption**: Decipher a emoji ciphertext message by displaying it in the predicted plaintext output.

## 🛠️ Installation

```sh
git clone https://github.com/321BadgerCode/substitution_symphony.git
cd ./substitution_symphony/
```

## 📈 Usage

### Encrypt

```sh
python ./encrypt.py <message>
# Or
echo <message> | python ./encrypt.py
```

#### Example

```sh
echo "abcdefghijklmnopqrstuvwxyz" | python ./encrypt.py # 😀😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙
```

### Decrypt

> [!WARNING]
> The deciphering of the emoji ciphertext was not yielding promising results, so currently the threshold values for the n-grams are peculiar and the program does not currently take in command line arguments. However, the plaintext in the program can easily be altered.
```sh
python ./main.py
```

## 📝 License

[LICENSE](./LICENSE)