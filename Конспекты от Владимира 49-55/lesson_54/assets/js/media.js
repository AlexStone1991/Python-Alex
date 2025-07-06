function enableFullscreenImages() {
  const fullscreenContainer = createFullscreenContainer();
  document.body.appendChild(fullscreenContainer);

  document.querySelectorAll("img").forEach((img) => {
    img.addEventListener("click", () =>
      showFullscreenImage(fullscreenContainer, img.src)
    );
  });

  fullscreenContainer.addEventListener("click", () => {
    fullscreenContainer.classList.remove("active");
  });
}

function createFullscreenContainer() {
  const container = document.createElement("div");
  container.classList.add("fullscreen-img-container");
  return container;
}

function showFullscreenImage(container, src) {
  const img = new Image();
  img.src = src;
  img.onload = function () {
    const screenRatio = window.innerWidth / window.innerHeight;
    const imageRatio = this.width / this.height;

    if (imageRatio > screenRatio) {
      img.style.width = "100vw";
      img.style.height = "auto";
    } else {
      img.style.width = "auto";
      img.style.height = "100vh";
    }
  };
  container.innerHTML = "";
  container.appendChild(img);
  container.classList.add("active");
}

function initVideoPlayer() {
  const videoElements = document.querySelectorAll("video");

  if (!videoElements.length) {
    console.log("На странице нет видео элементов");
    return;
  }

  if (typeof Plyr === "undefined") {
    console.log("Plyr не загружен");
    return;
  }

  Plyr.setup("video", {
    controls: [
      "play-large",
      "play",
      "progress",
      "current-time",
      "duration",
      "mute",
      "volume",
      "fullscreen",
    ],
    settings: ["speed"],
    speed: {
      selected: 1,
      options: [0.5, 1, 1.25, 1.5, 2, 2.25, 2.5],
    },
  });
}
