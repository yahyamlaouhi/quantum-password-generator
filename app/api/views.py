from django.shortcuts import render
import qiskit
from qiskit import QuantumCircuit, Aer, transpile, assemble
import numpy as np
import qiskit
from qiskit import QuantumCircuit
from qiskit.visualization import circuit_drawer
import io
import matplotlib.pyplot as plt
import base64
from .forms import PasswordForm

def generate_random_password(request):
    context={}
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        print("fffffffffffffffff",form.is_valid(),form.errors)

        if form.is_valid():

            num_qubits=form.cleaned_data["password_length"]
            password_length =form.cleaned_data["qubits_number"]
            print("fffffffffffffffff",num_qubits,password_length)
            # Define the number of qubits for the quantum register


            # Create a quantum circuit with the specified number of qubits
            quantum_circuit = QuantumCircuit(num_qubits)

            # Apply Hadamard gate to each qubit to create superposition
            for qubit in range(num_qubits):
                quantum_circuit.h(qubit)

            quantum_circuit.draw(output='mpl')

            # Measure the qubits
            quantum_circuit.measure_all()

            # Simulate the quantum circuit to generate random numbers
            simulator = Aer.get_backend('aer_simulator')
            compiled_circuit = transpile(quantum_circuit, simulator)
            job = simulator.run(assemble(compiled_circuit))
            result = job.result()
            counts = result.get_counts()

            # Convert the counts to a random number
            random_number = int(max(counts, key=counts.get), 2)

            # Generate a password based on the random number and user specifications
            def generate_password(length):
                characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?"
                password = ''.join(np.random.choice(list(characters), length))
                return password

            # User-defined password length


            # Generate the password
            password = generate_password(password_length)

            # Print the random number and generated password
            print("Random Number:", random_number)
            print("Generated Password:", password)
            quantum_circuit.draw(output='mpl')

            qc_image = io.BytesIO()
            circuit_drawer(quantum_circuit, output='mpl', scale=0.5).savefig(qc_image, format='png')
            encoded_image = base64.b64encode(qc_image.getvalue()).decode('utf-8')
            context = {'Qc_image': encoded_image,"Random_Number": random_number,"Generated_Password": password,'form': PasswordForm}
    else:
        form=PasswordForm()
        context = {'form': PasswordForm()}




            # Pass the image data to the template
    return render(request, 'index.html', context)
        
        
