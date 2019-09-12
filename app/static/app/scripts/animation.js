const logo = document.querySelectorAll("#logo path");
console.log(logo);
for (let i = 0; i < logo.length / 2; i++) {
    console.log('Letter ' + i + ' is  ' + logo[i].getTotalLength());
}
const logo2 = document.querySelectorAll("#logo2 path");
console.log(logo2);
for (let i = 0; i < logo2.length / 2 + 1; i++) {
    console.log('Letter ' + i + ' is  ' + logo2[i].getTotalLength());
}