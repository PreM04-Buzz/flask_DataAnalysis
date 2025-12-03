function sortTable(col) {
    let table = document.getElementById("mainTable");
    let rows = Array.from(table.rows).slice(1);
    let asc = table.getAttribute("data-sort") !== "asc";
    rows.sort((a, b) => {
        let x = a.cells[col].innerText.replace(/,/g, "");
        let y = b.cells[col].innerText.replace(/,/g, "");
        return asc ? x - y : y - x;
    });
    rows.forEach(r => table.appendChild(r));
    table.setAttribute("data-sort", asc ? "asc" : "desc");
}

function searchTable() {
    let input = document.getElementById("searchInput").value.toLowerCase();
    let rows = document.querySelectorAll("#mainTable tbody tr");
    rows.forEach(row => {
        row.style.display = row.innerText.toLowerCase().includes(input) ? "" : "none";
    });
}

