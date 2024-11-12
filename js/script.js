
const currencyOne = document.getElementById('currency');
const currencyTwo = document.getElementById('currency-two');
const amountOne = document.getElementById('amount-one');
const amountTwo = document.getElementById('amount-two');
const swapButton = document.getElementById('btn');
const rateText = document.getElementById('rateText');


function calculate() {
    const currency1 = currencyOne.value;
    const currency2 = currencyTwo.value;
    const amount = amountOne.value;


    fetch(`https://api.exchangerate-api.com/v4/latest/${currency1}`)
        .then(res => res.json())
        .then(data => {
            const rate = data.rates[currency2];
            rateText.innerText = `1 ${currency1} = ${rate} ${currency2}`;
            amountTwo.value = (amount * rate).toFixed(2);
        });
}


currencyOne.addEventListener('change', calculate);
currencyTwo.addEventListener('change', calculate);
amountOne.addEventListener('input', calculate);


swapButton.addEventListener('click', () => {
    const temp = currencyOne.value;
    currencyOne.value = currencyTwo.value;
    currencyTwo.value = temp;
    calculate();
});


calculate();
