function addRollNumber() {
  const rollInput = document.getElementById("rollInput");
  const rollList = document.getElementById("rollList");

  const rollNumber = rollInput.value.trim();

  if (rollNumber !== "") {
    const li = document.createElement("li");
    li.textContent = rollNumber;
    rollList.appendChild(li);
    rollInput.value = "";
  } else {
    alert("Please enter a roll number!");
  }
}



