(function() {
		
		let field = document.querySelector('.items');
		let li = Array.from(field.children);

		function FilterProduct() {
			for(let i of li){
				const name = i.querySelector('strong');
				const x = name.textContent;
				i.setAttribute("data-category", x);
			}

			let indicator = document.querySelector('.indicator').children;

			this.run = function() {
				for(let i=0; i<indicator.length; i++)
				{
					indicator[i].onclick = function () {
						for(let x=0; x<indicator.length; x++)
						{
							indicator[x].classList.remove('active');
						}
						this.classList.add('active');
						const displayItems = this.getAttribute('data-filter');

						for(let z=0; z<li.length; z++)
						{
							li[z].style.transform = "scale(0)";
							setTimeout(()=>{
								li[z].style.display = "none";
							}, 500);

							if ((li[z].getAttribute('data-category') == displayItems) || displayItems == "all")
							 {
							 	li[z].style.transform = "scale(1)";
							 	setTimeout(()=>{
									li[z].style.display = "block";
								}, 500);
							 }
						}
					};
				}
			}
		}

		function SortProduct() {
			let select = document.getElementById('select');
			let li = document.getElementsByTagName('li');
			let ar = [];
		
			for (let i of li) {
				const last = i.lastElementChild;
				const x = last.textContent.trim();
				const y = Number(x.substring(1));
				i.setAttribute("date", y);
				ar.push(i);
			}
		
			// Function to sort elements based on date
			function SortElem(field, li, asc) {
				let dm = asc ? 1 : -1;
				let sortli = Array.from(li).sort((a, b) => {
					const ax = parseInt(a.getAttribute('date'));
					const bx = parseInt(b.getAttribute('date'));
					return (ax - bx) * dm;
				});
		
				while (field.firstChild) {
					field.removeChild(field.firstChild);
				}
				field.append(...sortli);
			}
		
			// Set up event handling for sorting
			this.run = () => {
				addevent();
			}
		
			function addevent() {
				select.onchange = sortingValue;
			}
		
			function sortingValue() {
				const field = document.getElementById('select'); // Assuming this is the element where you want to display the sorted items.
		
				if (this.value === 'Default') {
					while (field.firstChild) {
						field.removeChild(field.firstChild);
					}
					field.append(...ar);
				}
				if (this.value === 'LowToHigh') {
					SortElem(field, li, true);
				}
				if (this.value === 'HighToLow') {
					SortElem(field, li, false);
				}
			}
		}
		

		new FilterProduct().run();
		new SortProduct().run();
	})();