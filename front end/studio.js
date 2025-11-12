document.addEventListener("DOMContentLoaded", () => {
  document.body.classList.add("js-enabled");

  const dropzone = document.querySelector("[data-dropzone]");
  const fileInput = dropzone?.querySelector('input[type="file"]') ?? null;
  const fileNameLabel = document.querySelector("[data-file-name]");
  const feedbackMessage = document.querySelector("[data-file-feedback]");
  const startButton = document.querySelector("[data-start-btn]");

  let selectedFile = null;

  const MAX_FILE_SIZE_BYTES = 50 * 1024 * 1024; // 50 MB

  const resetState = (options = { message: "Accepted file types: PDF" }) => {
    selectedFile = null;
    dropzone?.classList.remove("has-file");
    if (fileInput) {
      fileInput.value = "";
    }

    if (fileNameLabel) {
      fileNameLabel.textContent = "No file selected yet.";
    }

    if (feedbackMessage) {
      feedbackMessage.textContent = options.message;
      feedbackMessage.classList.remove("error");
    }

    if (startButton) {
      startButton.disabled = true;
    }
  };

  const isPdf = (file) => {
    if (!file) return false;
    if (file.type === "application/pdf") return true;
    return file.name?.toLowerCase().endsWith(".pdf") ?? false;
  };

  const formatSize = (bytes) => {
    const megabytes = bytes / (1024 * 1024);
    if (megabytes < 1) {
      const kilobytes = bytes / 1024;
      return `${kilobytes.toFixed(1)} KB`;
    }
    return `${megabytes.toFixed(1)} MB`;
  };

  const setFile = (file) => {
    if (!file) {
      resetState();
      return;
    }

    if (!isPdf(file)) {
      resetState({ message: "Please upload a PDF document." });
      if (feedbackMessage) {
        feedbackMessage.classList.add("error");
      }
      return;
    }

    if (file.size > MAX_FILE_SIZE_BYTES) {
      resetState({ message: "File exceeds the 50 MB size limit. Please upload a smaller PDF." });
      if (feedbackMessage) {
        feedbackMessage.classList.add("error");
      }
      return;
    }

    selectedFile = file;
    dropzone?.classList.add("has-file");

    if (fileNameLabel) {
      fileNameLabel.textContent = `${file.name} (${formatSize(file.size)})`;
    }

    if (feedbackMessage) {
      feedbackMessage.textContent = "Ready when you are — start the transformation!";
      feedbackMessage.classList.remove("error");
    }

    if (startButton) {
      startButton.disabled = false;
    }
  };

  if (dropzone && fileInput) {
    ["dragenter", "dragover"].forEach((eventName) => {
      dropzone.addEventListener(eventName, (event) => {
        event.preventDefault();
        dropzone.classList.add("is-dragover");
      });
    });

    ["dragleave", "dragend"].forEach((eventName) => {
      dropzone.addEventListener(eventName, () => {
        dropzone.classList.remove("is-dragover");
      });
    });

    dropzone.addEventListener("drop", (event) => {
      event.preventDefault();
      dropzone.classList.remove("is-dragover");
      if (!event.dataTransfer?.files?.length) return;
      const [file] = event.dataTransfer.files;
      setFile(file);
    });

    fileInput.addEventListener("change", (event) => {
      const input = event.target;
      if (!(input instanceof HTMLInputElement) || !input.files?.length) {
        resetState();
        return;
      }
      const [file] = input.files;
      setFile(file);
    });

    dropzone.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        fileInput.click();
      }
    });
  }

  if (startButton) {
    startButton.disabled = true;
    startButton.addEventListener("click", (event) => {
      if (!selectedFile) {
        event.preventDefault();
        if (feedbackMessage) {
          feedbackMessage.textContent = "Upload your PDF before starting the transformation.";
          feedbackMessage.classList.add("error");
        }
        return;
      }

      feedbackMessage?.classList.remove("error");
      feedbackMessage?.classList.add("success");
      feedbackMessage?.setAttribute("role", "status");
      feedbackMessage?.setAttribute("aria-live", "polite");
      if (feedbackMessage) {
        feedbackMessage.textContent = `Uploading ${selectedFile.name}... (Simulation)`;
      }

      startButton.disabled = true;

      setTimeout(() => {
        if (feedbackMessage) {
          feedbackMessage.textContent = "Upload received! Our animators will reach out shortly.";
        }
        resetState({
          message: "Accepted file types: PDF",
        });
      }, 2500);
    });
  }
});

