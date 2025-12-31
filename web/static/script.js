async function planTrip() {
    const query = document.getElementById("query").value;
    const output = document.getElementById("output");

    output.textContent = "Planning your trip...";

    const response = await fetch("/plan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query })
    });

    const data = await response.json();

    if (data.result) {
        output.textContent = data.result;
    } else {
        output.textContent = data.error;
    }
}
