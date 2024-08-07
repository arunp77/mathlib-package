const { exec } = require('child_process');

// Function to install Python package
function installPythonPackage() {
  exec('pip install ./MathLib', (error, stdout, stderr) => {
    if (error) {
      console.error(`Error: ${error.message}`);
      return;
    }
    if (stderr) {
      console.error(`stderr: ${stderr}`);
      return;
    }
    console.log(`stdout: ${stdout}`);
  });
}

installPythonPackage();
