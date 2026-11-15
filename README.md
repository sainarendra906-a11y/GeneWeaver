# GeneWeaver
## GPU-Accelerated CRISPR Alignment Engine

An internship project developed for Infotact Solutions.

### Implemented Modules

1. FASTA Parser
2. CPU-based DNA Sequence Alignment Engine
3. CPU Alignment Unit Tests

### CPU Alignment Features

- DNA sequence comparison
- Sliding-window alignment
- Mismatch counting
- Configurable mismatch threshold
- Case-insensitive matching

### Testing

Run CPU alignment tests:

```powershell
.\.venv\Scripts\python.exe -m unittest tests.test_alignment -v
