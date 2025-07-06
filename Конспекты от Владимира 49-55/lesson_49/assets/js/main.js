document.addEventListener("DOMContentLoaded", function () {
  console.log("DOMContentLoaded: Инициализация main.js");

  // Вызываем функции из разделённых модулей
  generateTableOfContents();
  addCodeCopyButtons();
  enableFullscreenImages();
  initVideoPlayer();

  // Центровка элементов
  const elementsToCenter = {
    img: ["img-fluid", "d-block", "mx-auto"],
    iframe: ["d-block", "mx-auto"],
    table: ["table", "table-striped"],
    video: ["d-block", "mx-auto"],
  };
  centerElements(elementsToCenter);

  // Обработка блоков цитат
  processBlockquotes();
});

function centerElements(elementsToCenter) {
  Object.entries(elementsToCenter).forEach(([tag, classes]) =>
    addClassesToElements(tag, classes)
  );
}

function addClassesToElements(tag, classes) {
  document.querySelectorAll(tag).forEach((el) => {
    classes.forEach((className) => el.classList.add(className));
  });
}

function processBlockquotes() {
    const blockquotes = document.querySelectorAll("blockquote");
    console.log("Найдено blockquotes:", blockquotes.length);
  
    blockquotes.forEach((blockquote, index) => {
      console.log(`Обработка blockquote #${index + 1}`);
  
      const firstP = blockquote.querySelector("p");
      if (firstP) {
        const text = firstP.textContent.trim();
        console.log(`Содержимое первого p: "${text}"`);
  
        const typeMapping = {
          "[!info]": "alert-info",
          "[!warning]": "alert-warning",
          "[!success]": "alert-success",
          "[!error]": "alert-error",
          "[!tip]": "alert-tip",
          "[!highlight]": "alert-highlight",
          "[!danger]": "alert-danger" // Добавлено для обработки dangerous-выноски
        };
  
        Object.entries(typeMapping).forEach(([marker, className]) => {
          if (text === marker) {
            console.log(
              `Найдено совпадение: ${marker} -> добавляем класс ${className}`
            );
            blockquote.classList.add(className);
            firstP.remove();
            console.log("Маркер удален");
          }
        });
      }
    });
  }
  
