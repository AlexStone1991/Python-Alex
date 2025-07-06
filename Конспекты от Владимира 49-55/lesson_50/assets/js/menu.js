function generateTableOfContents() {
  const toc = document.getElementById("table-of-contents");
  const headers = document.querySelectorAll("h2, h3");
  const ul = document.createElement("ul");

  if (headers.length === 0) {
    return;
  }

  headers.forEach((header, index) => {
    const li = document.createElement("li");
    const a = document.createElement("a");

    if (!header.id) {
      header.id = `header-${index}`;
    }

    a.href = `#${header.id}`;
    a.textContent = header.textContent;

    if (header.tagName === "H3") {
      li.style.marginLeft = "1.5rem";
    }

    li.appendChild(a);
    ul.appendChild(li);
  });

  toc.appendChild(ul);

  window.addEventListener("scroll", () => {
    const scrollPosition = window.scrollY;

    headers.forEach((header) => {
      const headerTop = header.offsetTop;
      const headerBottom = headerTop + header.offsetHeight;
      const link = toc.querySelector(`a[href="#${header.id}"]`);

      if (scrollPosition >= headerTop - 100 && scrollPosition < headerBottom) {
        link.classList.add("active");

        // Прокрутка оглавления, если активный пункт не виден
        const linkRect = link.getBoundingClientRect();
        const tocRect = toc.getBoundingClientRect();

        if (linkRect.bottom > tocRect.bottom) {
          toc.scrollTop += linkRect.bottom - tocRect.bottom;
        } else if (linkRect.top < tocRect.top) {
          toc.scrollTop -= tocRect.top - linkRect.top;
        }
      } else {
        link.classList.remove("active");
      }
    });
  });
}
