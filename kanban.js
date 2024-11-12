let activeCard = null;

function openCard(card) {
    activeCard = card;
    document.getElementById('modal-textarea').value = card.textContent;
    document.getElementById('modal').style.display = 'flex';
}

function saveText() {
    const textarea = document.getElementById('modal-textarea');
    if (activeCard) {
        activeCard.textContent = textarea.value;
    }
    closeModal();
}

function closeModal() {
    document.getElementById('modal').style.display = 'none';
    activeCard = null;
}

