document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".cloze").forEach(function (el) {
      // 最初にhiddenクラスを追加して隠す
      el.classList.add("hidden");
      
      el.addEventListener("click", function () {
        el.classList.toggle("hidden");
      });
    });
  });