/* Dynamically Rotating Text */

let i = 0;

const rotateText = () => {
  const phrase = document.querySelector(".rotating-text");
  const compStyles = window.getComputedStyle(phrase);
  const animation = compStyles.getPropertyValue("animation");
  const animationTime = parseFloat(animation.match(/\d*[.]?\d+/)) * 1000;

  const phrases = ["army", "fleet", "squad", "armada", "convoy", "legion", "militia", "infantry", "swarm", "horde", "platoon", "crew", "bridage", "company", "corps", "flotilla", "navy"];

  i = randomNum(i, phrases.length);
  const newPhrase = phrases[i];

  setTimeout(() => {
    phrase.textContent = newPhrase;
  }, 400); // Time for opacity to hit 0 before changing words.
};

const randomNum = (num, max) => {
  let j = Math.floor(Math.random() * max);

  // Ensure different number.
  if (num === j) {
    return randomNum(i, max);
  } else {
    return j;
  }
};

const getAnimationTime = () => {
  const phrase = document.querySelector(".rotating-text");
  const compStyles = window.getComputedStyle(phrase);
  let animation = compStyles.getPropertyValue("animation");

  const animationTime = parseFloat(animation.match(/\d*[.]?\d+/)) * 1000;
  return animationTime;
};

rotateText();
setInterval(rotateText, getAnimationTime());
