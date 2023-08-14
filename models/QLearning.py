import torch
import torch.nn as nn
import torch.optim as optim


# Definir la arquitectura de la red
class PerceptronMulticapa(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(PerceptronMulticapa, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        out = self.sigmoid(out)
        return out


# Parámetros de la red
input_size = 10
hidden_size = 32
output_size = 1

# Crear instancia de la red
red_neuronal = PerceptronMulticapa(input_size, hidden_size, output_size)

# Definir la función de pérdida y el optimizador
criterio = nn.BCELoss()  # Binary Cross-Entropy Loss
optimizador = optim.SGD(red_neuronal.parameters(), lr=0.01)

# Generar datos de ejemplo (solo para propósitos de ilustración)
num_samples = 1000
input_data = torch.randn(num_samples, input_size)
target_data = torch.randint(0, 2, (num_samples,), dtype=torch.float32)

# Entrenamiento de la red
num_epochs = 1000
for epoch in range(num_epochs):
    optimizador.zero_grad()  # Reiniciar gradientes
    outputs = red_neuronal(input_data)
    loss = criterio(outputs.squeeze(), target_data)
    loss.backward()  # Retropropagación
    optimizador.step()  # Actualizar pesos

    if (epoch + 1) % 100 == 0:
        print(f'Época [{epoch + 1}/{num_epochs}], Pérdida: {loss.item():.4f}')

# Evaluar la red entrenada (opcional)
with torch.no_grad():
    test_input = torch.randn(10, input_size)
    predictions = red_neuronal(test_input)
    print("Predicciones:", predictions)

# Guardar el modelo entrenado (opcional)
torch.save(red_neuronal.state_dict(), 'perceptron_multicapa.pth')
