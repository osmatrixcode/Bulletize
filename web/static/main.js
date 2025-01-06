
function changeButton(button) {
    // button.disabled = true;

    // Change button content
    button.innerHTML = `
    <div class="flex items-center">
<svg class="animate-spin h-5 w-5 mr-2 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
  <circle class="opacity-75" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" stroke-dasharray="31.4 78.5" stroke-linecap="round" transform="rotate(-90 12 12)"></circle>
</svg>
      <span>Processing...</span>
    </div>
  `;
}