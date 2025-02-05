$(document).ready(function () {
  const gravity = 9.8;
  const bounceDamping = 0.7;
  const groundLevel = 0;
  let bounceHeight = 300;

  function bounce() {
    const timeUp = Math.sqrt((2 * bounceHeight) / gravity);
    const timeDown = timeUp;

    $(".ball").animate(
      { bottom: `${bounceHeight}px` },
      timeUp * 100,
      "easeOutCubic",
      function () {
        $(".ball").animate(
          { bottom: `${groundLevel}px` },
          timeDown * 100,
          "easeInCubic",
          function () {
            bounceHeight *= bounceDamping;

            if (bounceHeight > 5) {
              bounce();
            }
          }
        );
      }
    );
  }

  bounce();
});
