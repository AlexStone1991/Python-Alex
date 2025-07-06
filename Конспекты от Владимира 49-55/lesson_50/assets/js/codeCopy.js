function addCodeCopyButtons() {
  document.querySelectorAll("pre").forEach((preBlock) => {
    preBlock.classList.add("pre-container");
    const copyButton = createCopyButton();
    preBlock.appendChild(copyButton);
    copyButton.addEventListener("click", () =>
      handleCopyButtonClick(preBlock, copyButton)
    );
  });
}

function createCopyButton() {
  const btn = document.createElement("i");
  btn.classList.add("bi", "bi-clipboard", "code-copy-btn");
  return btn;
}

function handleCopyButtonClick(preBlock, copyButton) {
  const codeElement = preBlock.querySelector("code");
  if (!codeElement) return;
  const codeContent = codeElement.innerText;
  navigator.clipboard.writeText(codeContent).then(() => {
    toggleCopyIcon(copyButton, true);
    setTimeout(() => toggleCopyIcon(copyButton, false), 3000);
  });
}

function toggleCopyIcon(copyButton, copied) {
  copyButton.classList.toggle("bi-clipboard", !copied);
  copyButton.classList.toggle("bi-clipboard-check", copied);

  if (copied) {
    copyButton.classList.add("copied");
    setTimeout(() => {
      copyButton.classList.remove("copied");
    }, 500);
  }
  copyButton.style.color = copied ? "lightgreen" : "white";
}
