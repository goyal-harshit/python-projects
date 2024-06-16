import fitz  # PyMuPDF


def extract_text_from_page(pdf_path, page_number):
	doc = fitz.open(pdf_path)
	page = doc.load_page(page_number)
	text = page.get_text()
	return text


def find_specific_information_in_pdf(pdf_path, keyword):
	doc = fitz.open(pdf_path)
	found_info = []

	for page_number in range(len(doc)):
		text = extract_text_from_page(pdf_path, page_number)
		if keyword in text:
			start_index = text.find(keyword)
			end_index = text.find('\n', start_index)
			specific_info = text[start_index:end_index]
			found_info.append((page_number, specific_info))

	return found_info


# Path to your PDF file
pdf_path = 'HARYANA-CO-OPERATIVE-SOCIETIES-ACT.pdf'

# Keyword to search for
keyword = 'Society'

# Find specific information in the PDF
specific_info_list = find_specific_information_in_pdf(pdf_path, keyword)

if specific_info_list:
	for page_number, info in specific_info_list:
		print(f'Found information on page {page_number + 1}: {info}')
else:
	print(f'Keyword "{keyword}" not found.')

