/**
 * This module have some
 * utils functions to use.
 */

/**
 * 
 * @param {HTMLElement} button The html button to get name
 * @returns The value of the game name
 */
export function getValuesToSend(button) {
  const gameName = button.parentElement.parentElement.childNodes[1].childNodes[1].innerText

  const startsPrice = button.parentElement.parentElement.childNodes[1].innerHTML

  return [gameName, startsPrice];

}