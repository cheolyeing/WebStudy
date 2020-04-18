function submit () {
	var url = 'https://webserver_edu_5e673a09eb2485ca52cb4358_flrzfgyjz.run.goorm.io/submit';
	fetch('/submit', {
		method: 'POST',
		headers: {'Content-Typez': 'application/json'},
		body: JSON.stringify({ })
	})
		.then(res => res.json())
		.then(ret => {
			var str = JSON.stringify(ret);
			console.log(str);
			// Update Element
		});
};