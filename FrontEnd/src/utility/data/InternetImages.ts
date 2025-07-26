const INTERNET_IMAGE_URLS = {
    1: 'https://cdn.thewirecutter.com/wp-content/media/2024/07/laptopstopicpage-2048px-3685-2x1-1.jpg?width=2048&quality=75&crop=2:1&auto=webp',
    2: 'https://cdn.thewirecutter.com/wp-content/media/2025/06/BEST-MONITORS-5504.jpg?auto=webp&quality=75&width=980&dpr=2',
    3: 'https://cdn.thewirecutter.com/wp-content/media/2023/07/bluetoothheadphones-2048px-6109-2x1-1.jpg?width=2048&quality=75&crop=2:1&auto=webp',
    4: 'https://hoekhome.com/cdn/shop/files/Desk_ONLY_Walnut_Black_GADs.jpg?v=1736356408&width=1100',
    5: 'https://cdn.thewirecutter.com/wp-content/media/2024/05/protablets-2048px-232469-2x1-1.jpg?width=2048&quality=75&crop=2:1&auto=webp',
    6: 'https://cdn.thewirecutter.com/wp-content/media/2023/05/desktopcomputer-2048px-8816-2x1-1.jpg?width=2048&quality=75&crop=2:1&auto=webp',
    7: 'https://cdn.thewirecutter.com/wp-content/media/2024/03/router-vs-modem-2048px-7397.jpg?auto=webp&quality=75&width=980&dpr=2',
    8: 'https://www.sikaic.com/cdn/shop/files/sikaic-office-chairs-brown-mid-century-faux-leather-leather-office-chair-with-arms-adjustable-back-40-brown-dj502642-43324019376436.jpg?v=1744251095&width=1000'
}

const DUMMY_ASSETS: _asset[] =[ 
    {id: 1, cathegory:'Electronics', desc: 'Laptop Computer', code: 'Asset_4398457A', url:INTERNET_IMAGE_URLS[1], quanity:21},
    {id: 2, cathegory:'Electronics', desc: 'Monitor', code: 'Asset_4398457B', url:INTERNET_IMAGE_URLS[2], quanity:40 },
    {id: 3, cathegory:'Electronics', desc: 'Headphones', code: 'Asset_4398457C', url:INTERNET_IMAGE_URLS[3], quanity:40 },
    {id: 4, cathegory:'Forniture', desc: 'Desk', code: 'Asset_4398457D', url:INTERNET_IMAGE_URLS[4], quanity:12 },
    {id: 5, cathegory:'Electronics', desc: 'Tablet', code: 'Asset_4398457E', url:INTERNET_IMAGE_URLS[5], quanity:30 },
    {id: 6, cathegory:'Electronics', desc: 'CPU', code: 'Asset_4398457F', url:INTERNET_IMAGE_URLS[6], quanity:40 },
    {id: 7, cathegory:'Electronics', desc: 'Modem', code: 'Asset_4398457G', url:INTERNET_IMAGE_URLS[7], quanity:4 },
    {id: 8, cathegory:'Forniture', desc: 'Chair', code: 'Asset_4398457I', url:INTERNET_IMAGE_URLS[8], quanity:12 },
]

type _asset = {
    id: number;
    cathegory: string;
    desc: string;
    code: string;
    quanity: number;
    url: string;
    qr?: '';
}

export {DUMMY_ASSETS, INTERNET_IMAGE_URLS};