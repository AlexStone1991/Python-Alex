window.addEventListener("load", function () {
  const NUM_SHAPES_MIN = 30;
  const NUM_SHAPES_MAX = 50;
  const MIN_SIZE = 7;
  const MAX_SIZE = 16;
  const MIN_BLUR = 3;
  const MAX_BLUR = 5;
  const EXTRA_BLUR = 2;
  const BASE_SPEED_RANGE = 40;
  const FRICTION = 0.99;
  const SCROLL_ACCEL_FACTOR = 0.003;
  const MAX_SPEED = 50;
  const REPEL_THRESHOLD = 100;
  const REPEL_FACTOR = 300;
  const WALL_MARGIN = 50;

  const shapesIcons = [
    "bi-robot",
    "bi-cpu",
    "bi-laptop",
    "bi-display",
    "bi-code-slash",
    "bi-terminal-fill",
    "bi-gear-fill",
    "bi-arrow-repeat",
    "bi-file-earmark-code",
    "bi-bug-fill",
    "bi-lightning-fill",
    "bi-diagram-3",
  ];

  let viewportWidth = window.innerWidth;
  let viewportHeight = window.innerHeight;
  let documentHeight = document.documentElement.scrollHeight;

  function updateDimensions() {
    viewportWidth = window.innerWidth;
    viewportHeight = window.innerHeight;
    documentHeight = document.documentElement.scrollHeight;
    parallaxContainer.style.height = documentHeight + "px";
  }

  window.addEventListener("resize", updateDimensions);

  const shapesCount =
    Math.floor(Math.random() * (NUM_SHAPES_MAX - NUM_SHAPES_MIN + 1)) +
    NUM_SHAPES_MIN;

  const parallaxContainer = document.createElement("div");
  parallaxContainer.classList.add("parallax-bg");
  parallaxContainer.style.height = documentHeight + "px";
  document.body.insertBefore(parallaxContainer, document.body.firstChild);

  const shapes = [];
  const contentArea = document.querySelector(".content-wrapper");

  for (let i = 0; i < shapesCount; i++) {
    const shapeElement = document.createElement("i");
    shapeElement.classList.add(
      "bi",
      shapesIcons[Math.floor(Math.random() * shapesIcons.length)],
      "parallax-shape"
    );

    const topPercent = Math.random() * 100;
    const leftPercent = Math.random() * 100;
    shapeElement.style.top = topPercent + "%";
    shapeElement.style.left = leftPercent + "%";

    const initX = (leftPercent / 100) * viewportWidth;
    const initY = (topPercent / 100) * documentHeight;

    const size = (Math.random() * (MAX_SIZE - MIN_SIZE) + MIN_SIZE).toFixed(2);
    shapeElement.style.fontSize = size + "rem";

    const baseBlur = parseFloat(
      (Math.random() * (MAX_BLUR - MIN_BLUR) + MIN_BLUR).toFixed(1)
    );
    shapeElement.style.filter = `blur(${baseBlur}px)`;

    let hue =
      Math.random() < 0.3
        ? Math.floor(Math.random() * 40) + 20
        : Math.floor(Math.random() * 360);
    shapeElement.style.color = `hsl(${hue}, 60%, 60%)`;

    const rotation = Math.floor(Math.random() * 361);

    const shapeObj = {
      element: shapeElement,
      posX: 0,
      posY: 0,
      initX: initX,
      initY: initY,
      speedX: (Math.random() - 0.5) * BASE_SPEED_RANGE,
      speedY: (Math.random() - 0.5) * BASE_SPEED_RANGE,
      baseBlur: baseBlur,
      rotation: rotation,
    };

    parallaxContainer.appendChild(shapeElement);
    shapes.push(shapeObj);
  }

  let lastScroll = window.scrollY;
  let lastTime = performance.now();

  function update() {
    updateDimensions();
    const now = performance.now();
    const dt = (now - lastTime) / 1000;
    const currentScroll = window.scrollY;
    const scrollDelta = Math.abs(currentScroll - lastScroll);
    const contentRect = contentArea
      ? contentArea.getBoundingClientRect()
      : null;

    shapes.forEach((shape) => {
      if (scrollDelta > 0) {
        const accel = 1 + scrollDelta * SCROLL_ACCEL_FACTOR;
        shape.speedX *= accel;
        shape.speedY *= accel;
      }

      shape.speedX *= FRICTION;
      shape.speedY *= FRICTION;

      const currentSpeed = Math.hypot(shape.speedX, shape.speedY);
      if (currentSpeed > MAX_SPEED) {
        const ratio = MAX_SPEED / currentSpeed;
        shape.speedX *= ratio;
        shape.speedY *= ratio;
      }

      shape.posX += shape.speedX * dt;
      shape.posY += shape.speedY * dt;

      let currentX = shape.initX + shape.posX;
      let currentY = shape.initY + shape.posY;

      if (currentX < WALL_MARGIN) {
        shape.posX = WALL_MARGIN - shape.initX;
        shape.speedX = Math.abs(shape.speedX);
      } else if (currentX > viewportWidth - WALL_MARGIN) {
        shape.posX = viewportWidth - WALL_MARGIN - shape.initX;
        shape.speedX = -Math.abs(shape.speedX);
      }

      if (currentY < WALL_MARGIN) {
        shape.posY = WALL_MARGIN - shape.initY;
        shape.speedY = Math.abs(shape.speedY);
      } else if (currentY > documentHeight - WALL_MARGIN) {
        shape.posY = documentHeight - WALL_MARGIN - shape.initY;
        shape.speedY = -Math.abs(shape.speedY);
      }

      let currentBlur = shape.baseBlur;
      if (contentRect) {
        const shapeRect = shape.element.getBoundingClientRect();
        if (
          shapeRect.top >= contentRect.top &&
          shapeRect.left >= contentRect.left &&
          shapeRect.bottom <= contentRect.bottom &&
          shapeRect.right <= contentRect.right
        ) {
          currentBlur = shape.baseBlur + EXTRA_BLUR;
        }
      }

      shape.element.style.filter = `blur(${currentBlur}px)`;
      shape.element.style.transform = `translate(${shape.posX}px, ${shape.posY}px) rotate(${shape.rotation}deg)`;
    });

    lastScroll = currentScroll;
    lastTime = now;
    requestAnimationFrame(update);
  }

  requestAnimationFrame(update);
});
