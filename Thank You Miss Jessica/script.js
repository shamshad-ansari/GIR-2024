document.getElementById("run-code-btn").addEventListener("click", () => {
  const outputImageContainer = document.getElementById(
    "output-image-container"
  );

  // Toggle display
  if (outputImageContainer.style.display === "block") {
    outputImageContainer.style.display = "none";
  } else {
    outputImageContainer.style.display = "block";
  }

  window.scrollBy(0, 900); // Scroll 200px down from the current position
});
