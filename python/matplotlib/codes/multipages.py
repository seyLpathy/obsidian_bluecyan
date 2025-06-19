import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
# Generate the data
data = np.random.randn(15, 1024)
# The PDF document
pdf_pages = PdfPages('barcharts.pdf')
# Generate the pages
plots_count = data.shape[0]
plots_per_page = 5
pages_count = int(np.ceil(plots_count / float(plots_per_page)))
grid_size = (plots_per_page, 1)
for i, samples in enumerate(data):
# Create a figure instance (ie. a new page) if needed
    if i % plots_per_page == 0:
        fig = plt.figure(figsize=(8.27, 11.69), dpi=100)
# Plot one bar chart
    plt.subplot2grid(grid_size, (i % plots_per_page, 0))
    plt.hist(samples, 32, normed=1, facecolor='.5', alpha=0.75)
# Close the page if needed
    if (i + 1) % plots_per_page == 0 or (i + 1) == plots_count:
        plt.tight_layout()
        pdf_pages.savefig(fig)
# Write the PDF document to the disk
pdf_pages.close()