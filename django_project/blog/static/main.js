function changeLike(id) {
    fetch('http://127.0.0.1:8000/api/post/'+ id, {method: "PUT"})
      .then(response => response.json())
      .then(json => {
        likeButton=document.getElementById("like-button")
        likeButton.innerHTML=json.liked ? "Unlike":"Like"
      })
  }
