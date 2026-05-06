console.log("テストデータ１")
document.addEventListener("DOMContentLoaded", async () => {
    const res = await fetch("/get_body_info/1");
    const data = await res.json();

    console.log("テストデータ２")
    console.log(data.height)

    document.getElementById("height").textContent = data.height;
    document.getElementById("weight").textContent = data.weight;
    document.getElementById("activity_status").textContent = data.activity_status_label;
})