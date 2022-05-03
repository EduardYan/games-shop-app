/*
	Principal javascript to use.
*/

import { getValuesToSend } from './utils.js';

// scrolling the cards
ScrollReveal().reveal('.card', {
  delay: 50,
});

// buttons manager
const buyButtons = document.querySelectorAll('.buy-button');

buyButtons.forEach(button => {
  button.addEventListener('click', () => {
    // getting the name of the game
    const values = getValuesToSend(button);

    // form to send
    const form = new FormData();
    form.append('game-name', values[0]);
    form.append('starts-price', values[1]);

    // sending
    fetch('/buy', {
        method: 'POST',
        body: form,
      })
      .then((res) => {
        if (res.ok) {
          console.log('--- Request send successfully ---');
        } else {
          throw '--- Some Error to send the request ---';
        }
      })
      .then((text) => {
        console.log(text);
      })
      .catch((err) => {
        console.log(err);
      })
  });
});